def pred(a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,q,r,s):
    import pandas as pd
    from sklearn.model_selection import train_test_split
    from sklearn.linear_model import LogisticRegression
    from sklearn.metrics import confusion_matrix
    from sklearn.metrics import classification_report
    df = pd.read_csv(r"covid_dataset.csv")
    df.head()
    df.isnull().sum()
    x = df.drop(["Sanitization from Market","Wearing Masks","COVID-19"],axis =1)
    y = df["COVID-19"]
    X_train,X_test,y_train,y_test = train_test_split(x,y,test_size = 0.4)
    log = LogisticRegression()
    log.fit(X_train,y_train)
    pred = log.predict(X_test)
    classification_report(pred,y_test)
    z = log.predict([[a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,q,r,s]])
    return z[0]
