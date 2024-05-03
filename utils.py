from crawler import crawl
import pandas as pd


def main():

    result_data = crawl()
            # Convert data to DataFrame
    df = pd.DataFrame([vars(item) for item in result_data])

    # Save DataFrame to CSV
    df.to_csv('stocks_data.csv', index=False)

    # Save DataFrame to JSON
    df.to_json('stocks_data.json', orient='records')

    # Save DataFrame to TSV
    df.to_csv('stocks_data.tsv', index=False, sep='\t')

if __name__ == '__main__':
    print("Running crawler")
    main()
