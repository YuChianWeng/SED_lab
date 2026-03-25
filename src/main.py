import sys
from src.parser import Parser
from src.utils.errors import CalculatorError

def main():
    """Main entry point for the interactive CLI calculator REPL."""
    print("Python CLI Calculator (type 'exit' or 'quit' to terminate)")
    while True:
        try:
            # Read input from user
            line = input(">>> ").strip()
            
            # Skip empty lines
            if not line:
                continue
            
            # Handle exit commands
            if line.lower() in ('exit', 'quit'):
                break
            
            # Parse and evaluate the expression
            parser = Parser(line)
            result = parser.parse()
            
            # Print the result (formatted as a float, or int if it's whole)
            if result == int(result):
                print(int(result))
            else:
                print(result)
            
        except (KeyboardInterrupt, EOFError):
            # Handle user interrupt gracefully
            print("\nExiting...")
            break
        except CalculatorError as e:
            # Report specific calculator errors (Lexer, Parser, Math) to stderr
            print(str(e), file=sys.stderr)
        except Exception as e:
            # Report unexpected errors to stderr
            print(f"Unexpected error: {e}", file=sys.stderr)

if __name__ == "__main__":
    main()
