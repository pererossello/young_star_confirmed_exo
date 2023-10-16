import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

def simp_figure(
    fig_size=100,
    fig_w=1080, fig_h=1080,
    text_size=1, grid=True, theme="dark",
    color='#000000',
    dpi=300,
    layout='constrained'
):
    ratio = fig_w / fig_h
    fig_width = fig_w / dpi
    fig_height = fig_h / dpi
    fig_size = fig_width * fig_height
    fs = np.sqrt(fig_size)
    fig = plt.figure(
        figsize=(fig_width, fig_height),
        dpi=dpi,  # Default dpi, will adjust later for saving
        layout=layout,
    )

    ax = fig.subplots()

    if theme == 'dark':
        fig.patch.set_facecolor(color)
        plt.rcParams.update({"text.color": "white"})
        ax.set_facecolor(color)
        ax.tick_params(colors="white")
        ax.spines["bottom"].set_color("white")
        ax.spines["top"].set_color("white")
        ax.spines["left"].set_color("white")
        ax.spines["right"].set_color("white")
        ax.xaxis.label.set_color("white")
        ax.yaxis.label.set_color("white")

    ax.xaxis.set_tick_params(which="minor", bottom=False)
    ax.tick_params(
        axis="both",
        which="major",
        labelsize=1.5 * text_size * fs,
        size=fs * 0.5,
        width=fs * 0.15,
    )
    if grid:
        ax.grid(
            which="major",
            linewidth=fs * 0.015,
            color="white" if theme == "dark" else "black",
        )
    for spine in ax.spines.values():
        spine.set_linewidth(fs * 0.15)

    # axes equal
    #ax.set_aspect("equal")
            
    return fig, ax, fs