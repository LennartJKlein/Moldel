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


class BarChartPrinter(Printer):
    """ The Bar Chart Printer prints a bar chart with the likelihoods that players are the Mol. """

    # Up to how many decimals the likelihoods will be rounded before printing them (if you do not round the likelihoods
    # then the pie chart will be cluttered).
    __PRECISION = 3

    def __init__(self, season, latest_episode, file_name: Union[str, None] = None):
        """ Constructor of the Bar Chart Printer.

        Parameters:
            file_name (Union[str, None]): If set then instead of showing a Bar Chart, it will save a Bar Chart as this
                given file name.
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

        plt.figure(dpi=300)
        plt.minorticks_on()
        plt.subplots_adjust(bottom=0.17, top=0.86, left=0.1, right=0.95)
        plt.gca().spines['bottom'].set_color('0.6')
        plt.gca().spines['top'].set_color('0.9')
        plt.gca().spines['right'].set_color('0.9')
        plt.gca().spines['left'].set_color('0.6')
        plt.gca().tick_params(axis="x", which="minor", bottom=False)
        plt.xticks(fontsize=9, rotation=-12)
        plt.gca().tick_params(axis='y', colors="#aaa")
        plt.grid(True, which="major", axis="y", color="#ddd", zorder=0)
        plt.grid(True, which="minor", axis="y", color="#eee", zorder=0, linestyle="--")
        plt.gca().yaxis.set_major_formatter(mtick.PercentFormatter(100))
        plt.ylim(0, 100)
        container = plt.bar(names, likelihoods, color=colors, zorder=3)
        plt.bar_label(container, fmt="%.1f%%", color="#000", zorder=4, padding=4)
        plt.gca().set_xticks(range(len(names)))
        plt.gca().set_xticklabels(names)

        def get_photo(name):
            path = "moldel/Data/Faces/{}-{}.jpg".format(self.__season, name.upper())
            if os.path.isfile(path):
                im = Image.open(path)
                smallestSize = min(im.width, im.height)
                offsetX = (im.width-smallestSize)/2 if (im.width-smallestSize) else 0
                offsetY = (im.height-smallestSize)/2 if (im.height-smallestSize) else 0
                im = im.resize((300, 300), resample=Image.Resampling.BICUBIC, box=(
                    offsetX, offsetY, smallestSize + offsetX, smallestSize + offsetY))

                mask = Image.new("L", (300, 300), 0)
                drawMask = ImageDraw.Draw(mask)
                drawMask.ellipse((0, 0, 300, 300), fill=255)
                bg = Image.new("RGBA", (300, 300), (255, 0, 0, 0))
                im = Image.composite(im, bg, mask)
                return im
            return None

        def insert_image(coord, name, ax):
            img = get_photo(name)
            if img:
                im = OffsetImage(img, zoom=0.1)
                im.image.axes = ax
                ab = AnnotationBbox(im, (coord, 0),  xybox=(0., -10), frameon=False,
                                    xycoords='data',  boxcoords="offset points", pad=0)
                ax.add_artist(ab)
                plt.gca().tick_params(axis='x', which='major', pad=24)

        for i, c in enumerate(names):
            insert_image(i, c, plt.gca())

        if (self.__latest_episode == 0):
            plt.title(
                r"$\bf{Overeenkomst\ met\ een\ Mol}$" + f"\n(voor seizoen {self.__season} begint)", fontname="Avenir")
        else:
            plt.title(
                r"$\bf{Overeenkomst\ met\ een\ Mol}$" + "\n(na aflevering " + f"{self.__latest_episode}, seizoen {self.__season})", fontname="Avenir")
        if self.__file_name is None:
            plt.show()
        else:
            plt.savefig(self.__file_name, dpi=150)
            source = tinify.from_file(self.__file_name + ".png")
            source.to_file(self.__file_name + ".png")
            plt.clf()
