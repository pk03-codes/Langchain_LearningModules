from langchain_text_splitters import RecursiveCharacterTextSplitter,Language

text="""
def calculate_sum(numbers):
    total = 0

    for number in numbers:
        total += number

    return total


def calculate_average(numbers):
    total = calculate_sum(numbers)
    return total / len(numbers)


def main():
    numbers = [10, 20, 30, 40, 50]

    total = calculate_sum(numbers)
    average = calculate_average(numbers)

    print("Total:", total)
    print("Average:", average)


if __name__ == "__main__":
    main()

"""

splitter=RecursiveCharacterTextSplitter.from_language(
    language=Language.PYTHON,
    chunk_size=100,
    chunk_overlap=25
)

chunk=splitter.split_text(text)

print(len(chunk))