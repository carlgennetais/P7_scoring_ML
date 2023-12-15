import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import seaborn as sns
from anytree import Node, RenderTree
# machine learning
from sklearn import decomposition

def print_correlation_matrix(df):
    """
    Print correlation matrix of df with :
        - only bottom triangle (upper is the same)
        - diverging colormap
        - annotations
    """
    plt.figure()
    sns.set_theme(style="white")  # for white background
    sns.heatmap(
            df.corr(),
            # shape
            mask=np.triu(df.corr()),
            square=True,
            linewidths=0.6,
            # diverging colormap
            cmap=plt.cm.RdBu,
            center=0,
            vmin=-1,
            vmax=1,
            # annotations
            annot=True,
            annot_kws={"size": 10},
            fmt=".2f",
            # cbar_kws={"shrink": 0.5},
            );


def myANOVA(dataframe, X_quanti, Y_quali, n_top=0):
    """
    Plots analysis of variance of a quantitive variable, 
    by a qualitative variable, sorted by median

    Parameters:
            dataframe (DataFrame): dataframe containing the other two variables
            X_quanti (float): quantitative variable
            Y_quali (object): qualitative variable
    """
    # Exclude NaN then group_by
    grouped = (
            dataframe.dropna(subset=[X_quanti, Y_quali])[[Y_quali, X_quanti]]
            .reset_index(drop=True)
            .groupby(Y_quali)
            )
    dfGrouped = pd.DataFrame({col: vals[X_quanti] for col, vals in grouped})

    # Sort by median
    meds = dfGrouped.median()
    meds.sort_values(ascending=True, inplace=True)
    dfGrouped = dfGrouped[meds.index]

    del meds, grouped

    # Colors and style
    medianprops = {"color": "yellow"}
    meanprops = {
            "marker": "o",
            "markeredgecolor": "red",
            "markerfacecolor": "red",
            }

    if n_top != 0:
        dfGrouped = dfGrouped.iloc[:, -n_top:]
        length = n_top / 3
    else:
        length = len(dataframe[Y_quali].unique()) / 3
    plt.figure(figsize=(10, length))
    plt.title("ANOVA of " + X_quanti + " by " + Y_quali)
    plt.xlabel(X_quanti)
    dfGrouped.boxplot(
            showfliers=False,
            medianprops=medianprops,
            vert=False,
            patch_artist=True,
            showmeans=True,
            meanprops=meanprops,
            )

    #     plt.legend(handles=[meanprops])
    plt.show();


def build_tree(df):
    """
    Build a tree from dataframe, with right-most cell as children 
    and left-most cell as parent. Uses Anytree library
    """
    # clean duplicated lines
    viz_categories = df.drop_duplicates()
    # create root node
    root_categories = Node("categories")
    # read cell by cell and build tree
    for i in range(0, viz_categories.shape[0]):
        for j in range(0, viz_categories.shape[1]):
            # if not empty and not already a Node
            if pd.notna(viz_categories.iloc[i, j]) and (
                    viz_categories.iloc[i, j] not in locals()
                    ):
                # for first level, attach to root
                if j == 0:
                    locals()[viz_categories.iloc[i, j]] = Node(
                            viz_categories.iloc[i, j], parent=root_categories
                            )
                # attach to n-1 parent
            else:
                locals()[viz_categories.iloc[i, j]] = Node(
                        viz_categories.iloc[i, j],
                        parent=locals()[viz_categories.iloc[i, j - 1]],
                        )
    return root_categories

def print_tree(tree, levels=2):
    """
    Print tree using Anytree library
    """
    for pre, fill, node in RenderTree(tree, maxlevel=levels):
        print("%s%s" % (pre, node.name))

# source : https://www.statology.org/seaborn-barplot-show-values/
def show_values(axs, orient="v", space=0.01):
    """
    Displays values next to bars for a horizontal or vertical bar plot.
    """

    def _single(ax):
        if orient == "v":
            for p in ax.patches:
                _x = p.get_x() + p.get_width() / 2
                _y = p.get_y() + p.get_height() + (p.get_height() * 0.01)
                value = "{:.2f}".format(p.get_height())
                ax.text(_x, _y, value, ha="center")
        elif orient == "h":
            for p in ax.patches:
                _x = p.get_x() + p.get_width() + float(space)
                _y = p.get_y() + p.get_height() - (p.get_height() * 0.5)
                value = "{:.2f}".format(p.get_width())
                ax.text(_x, _y, value, ha="left")

    if isinstance(axs, np.ndarray):
        for idx, ax in np.ndenumerate(axs):
            _single(ax)
    else:
        _single(axs)


def get_relation(df, col1, col2):
    """
    Returns relationship between 2 columns : 
    one-to-one, one-to-many, many-to-one or many-to-many
    """
    first_max = df[[col1, col2]].groupby(col1).count().max()[0]
    second_max = df[[col1, col2]].groupby(col2).count().max()[0]
    if first_max == 1:
        if second_max == 1:
            return "one-to-one"
        else:
            return "one-to-many"
    else:
        if second_max == 1:
            return "many-to-one"
        else:
            return "many-to-many"
