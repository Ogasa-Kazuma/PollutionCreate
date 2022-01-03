############################## ライブラリ  #####################################

import matplotlib.pyplot as plt

from mpl_toolkits.mplot3d.axes3d import Axes3D

import importlib

############################################################################

class PollutionScatterDrawer2D():

    def __init__(self, ax):

        self.__ax = ax
        self.__appearFunc = None

    def ApplyAppearanceFuncs(self, *functionObjs):
        for i in range(len(functionObjs)):
            functionObjs[i].func()



    def draw_pollution_map(self, xlim, ylim, pollutions, s_=20, marker_='o', cmap_=None, \
                           norm_=None, vmin_=None, vmax_=None, alpha_=None, linewidths_=None, \
                           verts_=None, edgecolors_=None, hold_=None, data_=None):

        new_x = []
        new_y = []
        new_pollutions = []

        for x_count in range(xlim):
            for y_count in range(ylim):
                new_x.append(x_count)
                new_y.append(y_count)
                new_pollutions.append(pollutions[x_count][y_count])


        sc = self.__ax.scatter(new_x, new_y, c = new_pollutions, cmap=cmap_)

        plt.show()










def main():



    fig = plt.figure()
    fig2 = plt.figure()
    pollution_state_drawer_2D = Pollution_State_Drawer_2D(fig, 131)
    pollution_state_drawer_2D_2 = Pollution_State_Drawer_2D(fig, 132)

    pollutions =  [[l for l in range(40)] for k in range(40)]
    for x_count in range(40):
        for y_count in range(40):
                pollutions[x_count][y_count] = 0.01 * x_count

    pollution_state_drawer_2D.draw_pollution_map(pollutions)
    pollution_state_drawer_2D_2.draw_pollution_map(pollutions)


if __name__ == "__main__":
    main()
