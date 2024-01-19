#!/usr/bin/ python
# -*- coding: utf-8 -*-


import matplotlib.pyplot as plt
import os


def get_plot(df, columns, plot_kind='bar', label_step=1, label_rotation=0,
             labels=None, title=None, save_path=None, **kwargs):
    """
    Generate a plot based on the provided DataFrame.

    Parameters:
    - df (pd.DataFrame): The input DataFrame containing the data for plotting.
    - columns (list): A list specifying the columns of the DataFrame to be used for plotting.
    - plot_kind (str, optional): The type of plot to be generated (e.g., 'bar', 'line', etc.). Defaults to 'bar'.
    - label_step (int, optional): The step size for x-axis tick labels. Defaults to 1.
    - label_rotation (int, optional): The rotation angle for x-axis tick labels. Defaults to 0.
    - labels (list, optional): Custom x-axis tick labels. If not provided, it uses the existing tick positions.
    - title (str, optional): The title of the plot. If not provided, a default title is generated.
    - **kwargs: Additional keyword arguments for customization.

    Returns:
    None
    """
    x_label = columns[0] if plot_kind != 'pie' else ''
    y_label = 'Count' if plot_kind != 'pie' else ''
    title = f'Counts' if title is None else title
    legend = None if len(columns) == 1 else columns[1]

    # Group data based on specified columns
    size_ = df.groupby(columns).size()
    counts = size_ if (len(columns) < 2) else size_.unstack().fillna(0)

    # Set the size of the figure
    _, ax = plt.subplots(figsize=(12, 8))

    # Plotting
    ax = counts.plot(kind=plot_kind, **kwargs)
    labels = ax.get_xticks()[::label_step] if labels is None else labels
    ax.set_xticks(labels)
    ax.set_xticklabels(ax.get_xticklabels(), rotation=label_rotation)

    # Customize plot labels and title
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)

    # Add legend if specified
    if legend:
        plt.legend(title=legend)

    # Save or display the plot
    if save_path:
        current_dir = os.getcwd()
        abs_path_to_file = os.path.join(current_dir, save_path)
        i = 0
        while os.path.exists(abs_path_to_file):
            i += 1
            base_name, ext = os.path.splitext(save_path)
            save_path = f"{base_name}_{i}{ext}"
            abs_path_to_file = os.path.join(current_dir, save_path)
        plt.savefig(save_path, bbox_inches='tight')
        print(f"Plot saved in ./{save_path}.")
    else:
        plt.show()
