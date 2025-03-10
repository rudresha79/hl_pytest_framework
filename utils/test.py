import pandas as pd


def read_excel_sheet_as_dict(file_path, sheet_name):
    # Read the specific sheet into a DataFrame
    df = pd.read_excel(file_path, sheet_name=sheet_name)
    # Convert DataFrame to list of dictionaries
    filtered_df = df[df['Execute'] == 'Yes']
    return filtered_df.to_dict(orient="records")


# Example usage
file_path = "C:/Users/rudre/PycharmProjects/PyTest_DataDriven_Framework/testdata/test_data.xlsx"
sheet_name = "Register"
data_list = read_excel_sheet_as_dict(file_path, sheet_name)

# Print the list of dictionaries
#print(data_list)

for x in data_list:
    print(x['URL'])