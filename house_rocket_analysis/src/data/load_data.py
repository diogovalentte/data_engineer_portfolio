def load_data(path):
    import pandas as pd
    data = pd.read_csv(path)

    # Sucess
    print('House Rocket dataset has been successfully loaded, has {} rows and {} columns.'.format(
        data.shape[0], data.shape[1]))

    return data
