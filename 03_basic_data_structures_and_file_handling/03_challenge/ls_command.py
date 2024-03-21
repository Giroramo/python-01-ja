import os


def ls_command(directory):
    # ユーザー入力が「sample」の場合、ディレクトリは「sample」になります
    # 無効なディレクトリパスについて考える必要はありません

    file_dict = {}
    
    # ディレクトリ内のファイルをスキャンし、拡張子ごとにファイルをまとめる
    for filename in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, filename)):
            # ファイルの拡張子を取得
            ext = os.path.splitext(filename)[1]            
            # 辞書に拡張子がなければ追加し、ファイル名をリストに追加
            if ext not in file_dict:
                file_dict[ext] = [filename]
            else:
                file_dict[ext].append(filename)
    
    # カテゴリごとのファイル数を表示
    print("Summary in alphabetical order:")
    for ext, files in sorted(file_dict.items()):
        print(f"{ext}:{len(files)} file{'s' if len(files) != 1 else ''}")



if __name__ == "__main__":
    directory_path = input("Enter directory path to organize files: ")

    if not os.path.isdir(directory_path):
        print("Invalid directory path.")
    else:
        ls_command(directory_path)
