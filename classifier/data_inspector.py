import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

DATASET_DIR = BASE_DIR / "datasets" / "processed"

def load_dataset(filename):

    filepath = DATASET_DIR / filename

    with open(filepath , "r" , encoding="utf-8") as f:
        return json.load(f)

def get_examples(dataset , intents):
    examples = {
        intent : []
        for intent in intents
    }

    for example in dataset:
        intent = example["intent"]

        if intent in examples:
            examples[intent].append(
                example["text"]
            )
    return examples

def print_examples(examples , limit = 50):
    for intent , questions in examples.items():
        print("\n" + "=" * 60)
        print(intent.upper())
        print("\n" + "=" * 60)

        for question in questions[:limit]:
            print(f"• {question}")

def main():
    dataset = load_dataset("train.json")

    intents = ["architecture" , "implementation" , "locate" , "casual"]

    examples = get_examples(dataset , intents)

    print_examples(examples , limit=30)

if __name__ == "__main__":
    main()