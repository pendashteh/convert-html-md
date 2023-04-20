import argparse
import os
import html2text

def convert_html_to_md(html_path, md_path):
    with open(html_path, 'r') as html_file:
        html_content = html_file.read()
        
        # Use html2text to convert the HTML to Markdown
        md_content = html2text.html2text(html_content)

    with open(md_path, 'w') as md_file:
        md_file.write(md_content)

if __name__ == '__main__':
    # Set up the command-line argument parser
    parser = argparse.ArgumentParser(description='Convert HTML to Markdown')
    parser.add_argument('input', metavar='INPUT_FILE',
                        help='Path to the input HTML file')
    parser.add_argument('output', metavar='OUTPUT_FILE',
                        help='Path to save the output MD file')
    
    # Parse the command-line arguments
    args = parser.parse_args()

    # Convert HTML to Markdown
    convert_html_to_md(args.input, args.output)

    # Print confirmation message
    print(f'Successfully converted {os.path.basename(args.input)} to Markdown and saved as {os.path.basename(args.output)}')