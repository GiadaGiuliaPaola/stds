# Do not modify these lines
__winc_id__ = "8c2e6882503c4baa9ce2e050497c3f2f"
__human_name__ = "stds"

# Add your code after this line
import sys

def main():

    if len(sys.argv) != 2:
        print("Usage: python main.py <character>")
        sys.exit(1)
    # TODO: read text from stdin
    char_to_remove = sys.argv[1]
    input_text = sys.stdin.read().strip()

    # TODO: Filter character given as an argument from the text
    removed_count = 0
    filtered_text = ''
    for char in input_text:
        if char != char_to_remove:
            filtered_text += char
        else:
            removed_count += 1
    
    # TODO: Print the result to stdout
    sys.stdout.write(filtered_text)

    # TODO: Print the total number of removed characters to stderr
    sys.stderr.write(str(removed_count))


if __name__ == "__main__":
    main()
