def clean_data(marks, x_col_names, y_col_name):
    """
    clean_data function clean the dataset to remove all null values 
    and encode non numeric data to numeric value

    """
    
    from sklearn.preprocessing import LabelEncoder
    # import pandas as pd

    # Remove all rows with y_col_name is undefined i.e. "NaN" 
    marks_nona = marks.dropna(subset=[y_col_name])

    # Copying marks to make a training set X
    X = marks_nona[x_col_names].copy(deep=True)

    # string encoded columns are converted to numeric using LabelEncoder
    encoded_columns = ["State","Use computer", "Subjects"]

    le = LabelEncoder()
    # le_state = LabelEncoder()
    # le_subject = LabelEncoder()
    # le_use_comp = LabelEncoder()
    X["State"] = le.fit_transform(X["State"])
    X["Subjects"] = le.fit_transform(X["Subjects"])
    X["Use computer"] = le.fit_transform(X["Use computer"].fillna(value="0"))

    # featureset X
    print("Shape of X\t:",X.shape)

    # target variable y 
    y = marks_nona[y_col_name]
    print ("Shape of y\t:",y.shape)
    
    return X, y