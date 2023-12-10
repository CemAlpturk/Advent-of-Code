from dataclasses import dataclass
from collections import Counter


card_map = {
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "T": 10,
    "J": 11,
    "Q": 12,
    "K": 13,
    "A": 14,
}

card_map_joker = {
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "T": 10,
    "J": 1,
    "Q": 11,
    "K": 12,
    "A": 13,
}


def is_five_of_a_kind(hand: str) -> bool:
    # Check if the hand is five of a kind
    return len(set(hand)) == 1


def is_four_of_a_kind(hand: str) -> bool:
    # Check if the hand is four of a kind
    counts = Counter(hand)
    return 4 in counts.values()


def is_full_house(hand: str) -> bool:
    # Check if the hand is full house
    counts = Counter(hand)
    return 3 in counts.values() and 2 in counts.values()


def is_three_of_a_kind(hand: str) -> bool:
    # Check if the hand is three of a kind
    counts = Counter(hand)
    return 3 in counts.values() and 2 not in counts.values()


def is_two_pairs(hand: str) -> bool:
    # Check if the hand is two pairs
    counts = Counter(hand)
    return list(counts.values()).count(2) == 2


def is_one_pair(hand: str) -> bool:
    # Check if the hand is one pair
    counts = Counter(hand)
    return 2 in counts.values()


def is_high_card(hand: str) -> bool:
    # Check if the hand is high card
    counts = Counter(hand)
    return len(counts) == 5


def hand_type(hand: str) -> int:
    # Compute the type of hand
    # Five of a kind -> 7
    # Four of a kind -> 6
    # Full house -> 5
    # Three of a kind -> 4
    # Two pairs -> 3
    # One pair -> 2
    # High card -> 1

    if is_five_of_a_kind(hand):
        return 7
    elif is_four_of_a_kind(hand):
        return 6
    elif is_full_house(hand):
        return 5
    elif is_three_of_a_kind(hand):
        return 4
    elif is_two_pairs(hand):
        return 3
    elif is_one_pair(hand):
        return 2
    elif is_high_card(hand):
        return 1
    else:
        return 0


def hand_combinations(hand: str) -> list[str]:
    # Compute all possible hands from the given hand
    # by replacing the jokers with all possible cards
    # and return the list of hands

    # Find the number of jokers
    deck = set("23456789TJQKA")
    jokers = hand.count("J")

    if jokers == 0:
        return [hand]

    hands = [hand]
    for _ in range(jokers):
        new_hands = []
        for hand in hands:
            joker_index = hand.index("J")
            for card in deck:
                new_hands.append(hand[:joker_index] + card + hand[joker_index + 1 :])
        hands = new_hands

    return hands


def enhance_hand(hand: str) -> str:
    # Bad implementation
    # Compute all combinations of jokers to find
    # the best hand
    hands = hand_combinations(hand)
    types = [hand_type(hand) for hand in hands]
    # print(hands, types)
    max_type = max(types)
    idx = types.index(max_type)
    max_hand = hands[idx]
    # print(max_type)
    for i, hand in enumerate(hands):
        if types[i] < max_type:
            continue
        for c1, c2 in zip(hand, max_hand):
            if card_map_joker[c1] > card_map_joker[c2]:
                max_hand = hand
                break
            elif card_map[c1] < card_map[c2]:
                break

    return max_hand


@dataclass
class Hand:
    cards: str
    joker: bool = False

    def __post_init__(self) -> None:
        # Compute the type of hand
        if self.joker:
            enhanced = enhance_hand(self.cards)
            self.type = hand_type(enhanced)
        else:
            self.type = hand_type(self.cards)

    def __repr__(self) -> str:
        return f"Hand(cards={self.cards}, type={self.type})"

    def __lt__(self, other: "Hand") -> bool:
        if self.type < other.type:
            return True
        elif self.type > other.type:
            return False
        else:
            # Same type
            if self.joker:
                _map = card_map_joker
            else:
                _map = card_map
            for c1, c2 in zip(self.cards, other.cards):
                if _map[c1] < _map[c2]:
                    return True
                elif _map[c1] > _map[c2]:
                    return False
            return False

    def __eq__(self, other: "Hand") -> bool:
        if self.type == other.type:
            if self.joker:
                _map = card_map_joker
            else:
                _map = card_map
            for c1, c2 in zip(self.cards, other.cards):
                if _map[c1] != _map[c2]:
                    return False
            return True
        else:
            return False


def part1(filename: str) -> None:
    with open(filename) as f:
        lines = f.readlines()

    hands = []
    bids = []
    for line in lines:
        hand, bid = line.split()
        hands.append(Hand(hand))
        bids.append(int(bid))

    sorted_bids = [bid for _, bid in sorted(zip(hands, bids))]

    sum = 0
    for i, bid in enumerate(sorted_bids):
        sum += bid * (i + 1)

    print(sum)


def part2(filename: str) -> None:
    with open(filename) as f:
        lines = f.readlines()

    hands = []
    bids = []

    for line in lines:
        hand, bid = line.split()
        hands.append(Hand(hand, joker=True))
        bids.append(int(bid))

    sorted_bids = [bid for _, bid in sorted(zip(hands, bids))]

    sum = 0
    for i, bid in enumerate(sorted_bids):
        sum += bid * (i + 1)

    print(sum)


if __name__ == "__main__":
    part1("input.txt")
    part2("input.txt")
