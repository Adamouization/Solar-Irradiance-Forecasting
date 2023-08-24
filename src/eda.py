def plot_time_series(df, time_col, plot_cols):
    plot_features = df[plot_cols]
    plot_features.index = df[time_col]
    _ = plot_features.plot(subplots=True, rot=90, figsize=(15, len(plot_cols)))


def print_df_index_date_range(df, sample_str: str):
    print("{sample} dataset date ranges = {date_min} to {date_max}".format(
        sample=sample_str,
        date_min=min(df.index), 
        date_max=max(df.index)
    ))
    print()
