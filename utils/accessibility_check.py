import json
import os

report_path='accessibility_report.json'

def run_accessibility(page):
    # Inject axe-core library
    page.add_script_tag(url='https://cdnjs.cloudflare.com/ajax/libs/axe-core/4.3.2/axe.min.js')

    # Run accessibility checks
    results = page.evaluate('''() => {
        return new Promise((resolve) => {
            axe.run({}, (err, results) => {
                if (err) {
                    console.error(err);
                    resolve(null);
                }
                resolve(results);
            });
        });
    }''')

    # Prepare the data to be written
    report_data = {
        'page': page.url,
        'results': results
    }

    # Check if the report file exists
    if os.path.exists(report_path):
        # If it exists, read the existing data
        with open(report_path, 'r') as file:
            existing_data = json.load(file)
    else:
        # If it does not exist, initialize an empty list
        existing_data = []

    # Append the new results to the existing data
    existing_data.append(report_data)

    # Write the updated data to the file
    with open(report_path, 'w') as file:
        json.dump(existing_data, file, indent=2)
