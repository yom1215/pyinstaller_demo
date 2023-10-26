import os
from datetime import datetime
import pandas as pd
from sklearn.linear_model import LinearRegression

def create_folder_with_timestamp():
    # 現在の日時を取得
    now = datetime.now()

    # 日時を文字列にフォーマット
    folder_name = now.strftime("predict_%H%M")
    return folder_name

def perform_regression(train_file, test_file):
    # データの読み込み
    print('load data...')
    train_data = pd.read_csv(train_file)
    test_data = pd.read_csv(test_file)

    # 説明変数と目的変数を分離
    X_train = train_data.drop("target", axis=1)
    y_train = train_data["target"]
    X_test = test_data

    # 線形回帰モデルを訓練
    print('train model')
    model = LinearRegression()
    model.fit(X_train, y_train)

    # 予測
    print('predict test data')
    predictions = model.predict(X_test)

    return predictions

def main():
    folder_name = create_folder_with_timestamp()
    current_directory = os.getcwd()  # 現在のディレクトリを取得
    predicted_directory = os.path.join(current_directory, folder_name)

    if not os.path.exists(predicted_directory):
        os.mkdir(predicted_directory)  # predictedディレクトリがない場合は作成

    train_file = os.path.join(current_directory, "train.csv")
    test_file = os.path.join(current_directory, "test.csv")
    output_file = os.path.join(predicted_directory, "prediction.csv")

    predictions = perform_regression(train_file, test_file)

    # 予測結果をCSVとして保存
    print('save predictions...')
    pd.DataFrame(predictions, columns=["prediction"]).to_csv(output_file, index=False)

if __name__ == "__main__":
    main()
