def plot_time_series(df, time_col, plot_cols):
    plot_features = df[plot_cols]
    plot_features.index = df[time_col]
    _ = plot_features.plot(subplots=True, rot=90, figsize=(15, len(plot_cols)))


