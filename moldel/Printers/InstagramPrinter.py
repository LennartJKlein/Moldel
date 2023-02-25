from collections import deque
from Data.Player import Player
from Data.PlayerData import get_name
from iteround import saferound
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
from PIL import Image, ImageDraw
from Printers.Printer import Printer
from typing import Dict, Union, List
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import numpy as np
import os
import seaborn as sns
import tinify
tinify.key = "qN_KsJ5knq7PxpkJlRz1QurKzglsMAiB"


class InstagramPrinter(Printer):
    """ The Instagram Printer prints a reel-sizes bar chart with the likelihoods that players are the Mol. """

    # Up to how many decimals the likelihoods will be rounded before printing them (if you do not round the likelihoods
    # then the pie chart will be cluttered).
    __PRECISION = 3

    def __init__(self, season, latest_episode, file_name: Union[str, None] = None):
        """ Constructor of the Instagram Printer.

        Parameters:
            file_name (Union[str, None]): If set, the image will be saved as this filename
        """
        self.__season = season
        self.__latest_episode = latest_episode
        self.__file_name = file_name

    def print(self, distribution: Dict[Player, float]):
        palette = sns.color_palette("viridis", len(distribution))
        names = []
        likelihoods = []
        colors = []

        i = 0
        for playerEstimation in sorted(distribution.items(), key=lambda x: x[1]):
            likelihood = playerEstimation[1]
            if likelihood != 0:
                names.append(get_name(playerEstimation[0]))
                likelihoods.append(likelihood * 100)
                colors.append(palette[i])
            i += 1

        likelihoods_sum = sum(likelihoods)
        likelihoods = saferound([(likelihood / likelihoods_sum * 100) for likelihood in likelihoods], self.__PRECISION)

        plt.figure(dpi=300, figsize=[9, 16])
        plt.subplots_adjust(bottom=0.11, top=0.87, left=0.24, right=0.83)
        plt.gca().spines["bottom"].set_color("0.6")
        plt.gca().spines["left"].set_color("0.6")
        plt.gca().spines["right"].set_color("0.9")
        plt.gca().spines["top"].set_color("0.9")
        plt.grid(True, which="major", axis="x", color="#ddd", zorder=0)
        plt.grid(True, which="minor", axis="x", color="#eee", zorder=0, linestyle="--")
        plt.minorticks_on()
        plt.gca().tick_params(axis="y", which="minor", bottom=False)
        plt.gca().tick_params(axis="x", colors="#aaa")
        plt.yticks(fontsize=18, rotation=13, fontname="Avenir Next")
        plt.xticks(fontsize=18, fontname="Avenir")
        plt.gca().xaxis.set_major_formatter(mtick.PercentFormatter(100))
        plt.xlim(0, 100)
        container = plt.barh(names, likelihoods, color=colors, zorder=3)
        plt.bar_label(container, fmt="%.1f%%", color="#000", fontname="Avenir Next", fontsize=18, zorder=4, padding=8)
        plt.gca().set_yticks(range(len(names)))
        plt.gca().set_yticklabels(names)

        def get_photo(name):
            path = "moldel/Data/Faces/{}-{}.jpg".format(self.__season, name.upper())
            if os.path.isfile(path):
                im = Image.open(path)
                smallestSize = min(im.width, im.height)
                offsetX = (im.width-smallestSize)/2 if (im.width-smallestSize) else 0
                offsetY = (im.height-smallestSize)/2 if (im.height-smallestSize) else 0
                im = im.resize((400, 400), resample=Image.Resampling.BICUBIC, box=(
                    offsetX, offsetY, smallestSize + offsetX, smallestSize + offsetY))

                mask = Image.new("L", (400, 400), 0)
                drawMask = ImageDraw.Draw(mask)
                drawMask.ellipse((0, 0, 400, 400), fill=255)
                bg = Image.new("RGBA", (400, 400), (255, 0, 0, 0))
                im = Image.composite(im, bg, mask)
                return im
            return None

        def insert_image(coord, name, ax):
            img = get_photo(name)
            if img:
                im = OffsetImage(img, zoom=0.14)
                im.image.axes = ax
                ab = AnnotationBbox(im, (0, coord),  xybox=(0, 0.), frameon=False,
                                    xycoords="data",  boxcoords="offset points", pad=0)
                ax.add_artist(ab)
                plt.gca().tick_params(axis="y", which="major", pad=30)

        for i, c in enumerate(names):
            insert_image(i, c, plt.gca())

        if (self.__latest_episode == 0):
            plt.title(
                r"$\bf{Overeenkomst\ met\ een\ Mol}$" + f"\n(voor seizoen 2023 begint)",
                fontname="Avenir",
                fontsize=28
            )
        else:
            plt.title(
                r"$\bf{Overeenkomst\ met\ een\ Mol}$" +
                "\n(na aflevering " + f"{self.__latest_episode}, seizoen 2023)",
                fontname="Avenir",
                fontsize=28
            )
        if self.__file_name is None:
            plt.show()
        else:
            plt.savefig(self.__file_name, dpi=150)
            source = tinify.from_file(self.__file_name + ".png")
            source.to_file(self.__file_name + ".png")
            plt.clf()
