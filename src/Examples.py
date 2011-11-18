#--------------------------------------------------------------------------
# File and Version Information:
#  $Id$
#
# Description:
#  Module Examples...
#
#------------------------------------------------------------------------

"""This module provides examples of how to get and use the CSPad image

This software was developed for the SIT project.  If you use all or 
part of it, please give an appropriate acknowledgment.

@see RelatedModule

@version $Id: 2011-11-18$

@author Mikhail S. Dubrovin
"""

#------------------------------
#  Module's version from CVS --
#------------------------------
__version__ = "$Revision: 4 $"
# $Source$

#----------
#  Imports 
#----------
import sys
import os

import CalibPars          as calp
import CSPadConfigPars    as ccp
import CSPadImageProducer as cip

import GlobalGraphics     as gg # For test purpose in main only
import HDF5Methods        as hm # For test purpose in main only

#----------------------------------------------

def main_example_cxi() :

    print 'Start test in main_example_cxi()'

    #path_calib = '/reg/d/psdm/CXI/cxi37411/calib/CsPad::CalibV1/CxiDsd.0:Cspad.0'
    #path_calib = '/reg/d/psdm/CXI/cxi35711/calib/CsPad::CalibV1/CxiDs1.0:Cspad.0'
    path_calib  = '/reg/d/psdm/CXI/cxi37411/calib/CsPad::CalibV1/CxiDs1.0:Cspad.0'

    #fname  = '/reg/d/psdm/CXI/cxi35711/hdf5/cxi35711-r0009.h5'
    #fname  = '/reg/d/psdm/CXI/cxi37411/hdf5/cxi37411-r0080.h5'
    fname   = '/reg/d/psdm/CXI/cxi37411/hdf5/cxi37411-r0039.h5'

    #dsname = '/Configure:0000/Run:0000/CalibCycle:0000/CsPad::ElementV2/CxiDsd.0:Cspad.0/data'
    dsname  = '/Configure:0000/Run:0000/CalibCycle:0000/CsPad::ElementV2/CxiDs1.0:Cspad.0/data'
    event   = 0

    print 'Load calibration parameters from', path_calib 
    calp.calibpars.setCalibParsForPath ( run  = 1, path = path_calib )

    print 'Get raw CSPad event %d from file %s \ndataset %s' % (event, fname, dsname)
    ds1ev = hm.getOneCSPadEventForTest( fname, dsname, event )
    print 'ds1ev.shape = ',ds1ev.shape

    print 'Make the CSPad image from raw array'
    cspadimg = cip.CSPadImageProducer()
    arr = cspadimg.getImageArrayForCSPadElement( ds1ev )

    print 'Plot CSPad image'
    gg.plotImage(arr,range=(-10,90),figsize=(11.6,10))
    gg.move(200,100)
    gg.plotSpectrum(arr,range=(-10,90))
    gg.move(50,50)
    #gg.plotImageAndSpectrum(arr,range=(1,2001))
    print 'To EXIT the test click on "x" in the top-right corner of each plot window.'
    gg.show()

#----------------------------------------------

def main_example_xpp() :

    print 'Start test in main_example_xpp()'

    path_calib = '/reg/d/psdm/xpp/xpp47712/calib/CsPad::CalibV1/XppGon.0:Cspad.0'
    fname      = '/reg/d/psdm/xpp/xpp47712/hdf5/xpp47712-r0043.h5'
    dsname     = '/Configure:0000/Run:0000/CalibCycle:0000/CsPad::ElementV2/XppGon.0:Cspad.0/data'
    event      = 0

    print 'Load calibration parameters from', path_calib 
    calp.calibpars.setCalibParsForPath ( run  = 1, path = path_calib )

    print 'Get raw CSPad event %d from file %s \ndataset %s' % (event, fname, dsname)
    ds1ev = hm.getOneCSPadEventForTest( fname, dsname, event )
    print 'ds1ev.shape = ',ds1ev.shape

    print 'Make the CSPad image from raw array'
    cspadimg = cip.CSPadImageProducer()
    arr = cspadimg.getImageArrayForCSPadElement( ds1ev )

    print 'Plot CSPad image'
    gg.plotImage(arr,range=(0,2000),figsize=(11.6,10))
    gg.move(200,100)
    gg.plotSpectrum(arr,range=(0,2000))
    gg.move(50,50)
    print 'To EXIT the test click on "x" in the top-right corner of each plot window.'
    gg.show()

#----------------------------------------------

if __name__ == "__main__" :

    #main_example_cxi()
    main_example_xpp()
    sys.exit ( 'End of test.' )

#----------------------------------------------
