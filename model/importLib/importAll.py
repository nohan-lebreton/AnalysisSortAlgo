# file to simplify imports

# Turn off the message "Hello from the pygame community. ..."
################################################################################
from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pygame
################################################################################

# List Generator
################################################################################
from model.generator.Generator import Generator
################################################################################

# Comparison Counter & Array Accesses
################################################################################
from model.sort.FloatCompare import FloatCompare
from model.sort.MonitoredList import MonitoredList
################################################################################

# draw
################################################################################
from view.visualization.Window import Window
from model.visualization.Pipe import Pipe
from view.visualization.PipeDrawing import PipeDrawing
################################################################################

# algorithms
################################################################################
from model.sort.Sort import Sort
from model.sort.sortAlgo.SelectionSort import SelectionSort
from model.sort.sortAlgo.BubbleSort import BubbleSort
from model.sort.sortAlgo.InsertionSort import InsertionSort
from model.sort.sortAlgo.CountingSort import CountingSort
from model.sort.sortAlgo.HeapSort import HeapSort
from model.sort.sortAlgo.MergeSort import MergeSort
from model.sort.sortAlgo.QuickSort import QuickSort
from model.sort.sortAlgo.ShellSort import ShellSort
from model.sort.sortAlgo.GnomeSort import GnomeSort
from model.sort.sortAlgo.PancakeSort import PancakeSort
from model.sort.sortAlgo.CombSort import CombSort
from model.sort.sortAlgo.BogoSort import BogoSort
################################################################################

#tests
################################################################################
from unittesting.Run_tests import Run_tests
################################################################################











