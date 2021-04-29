import os

import liibattery3d
from liibattery3d import liib3d

data_path = os.path.join(liibattery3d.__path__[0], 'data')


def test_fit():
    """
    Test case for curve fit module to 3d lithium ion battery
    test the output size in an array of three elements corresponding
    to the optimized, desired, paramters: the characteristic time tau,
    the n fractor, and specific capacity Q
    """
    filepath = os.path.join(data_path, "capacityratepaper1set1.csv")
    # parameters
    tau = 0.5
    n = 1
    Qcapacity = 100
    params0 = [tau, n, Qcapacity]  # intial guess parameter
    popt = liib3d.fit(filepath, params0)
    try:
        lenparam = len(popt)
        assert(lenparam == 3)
    except AssertionError:
        print(f'I should have only three parameters, \
              not {lenparam}')
#    return


# def test_fitfunc():
#   '''
#   The output of the fit function is the (mass) normalize capacity
#   simply assert that the size of the output array is equal to the
#   size of the input array, and that
#   the maximum value at initail discharge rate (at zero) is equal to
#   the specific capacity
#   '''
#   return
