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
import numpy              as np

import PyCSPadImage.CalibPars          as calp
import PyCSPadImage.CalibParsEvaluated as cpe
import PyCSPadImage.CSPadConfigPars    as ccp
import PyCSPadImage.CSPadImageProducer as cip
import PyCSPadImage.CSPADPixCoords     as pixcoor
import PyCSPadImage.PixCoords2x1       as pixcoor2x1


import PyCSPadImage.GlobalGraphics     as gg # For test purpose in main only
import PyCSPadImage.GlobalMethods      as gm # For test purpose in main only
import PyCSPadImage.HDF5Methods        as hm # For test purpose in main only

#----------------------------------------------

def main_example_cxi() :

    print 'Start test in main_example_cxi()'

    #path_calib = '/reg/d/psdm/CXI/cxi35711/calib/CsPad::CalibV1/CxiDs1.0:Cspad.0'
    #path_calib = '/reg/d/psdm/CXI/cxi37411/calib/CsPad::CalibV1/CxiDsd.0:Cspad.0'
    #path_calib = '/reg/d/psdm/CXI/cxi37411/calib/CsPad::CalibV1/CxiDs1.0:Cspad.0'
    path_calib = '/reg/d/psdm/CXI/cxii0212/calib/CsPad::CalibV1/CxiDs1.0:Cspad.0'

    #fname, runnum   = '/reg/d/psdm/CXI/cxi35711/hdf5/cxi35711-r0009.h5', 9
    #fname, runnum   = '/reg/d/psdm/CXI/cxi37411/hdf5/cxi37411-r0080.h5', 80
    #fname, runnum    = '/reg/d/psdm/CXI/cxi37411/hdf5/cxi37411-r0039.h5', 39
    fname, runnum    = '/reg/d/psdm/CXI/cxii0212/hdf5/cxii0212-r0051.h5', 39

    #dsname = '/Configure:0000/Run:0000/CalibCycle:0000/CsPad::ElementV2/CxiDsd.0:Cspad.0/data'
    dsname  = '/Configure:0000/Run:0000/CalibCycle:0000/CsPad::ElementV2/CxiDs1.0:Cspad.0/data'
    event   = 5

    print 'Load calibration parameters from', path_calib
    calibpars = calp.CalibPars()
    calibpars.setCalibParsForPath ( run=runnum, path=path_calib )

    print 'Get raw CSPad event %d from file %s \ndataset %s' % (event, fname, dsname)
    ds1ev = hm.getOneCSPadEventForTest( fname, dsname, event )
    #ds1ev = hm.getAverageCSPadEvent( fname, dsname, event, nevents=50 )
    print 'CSPad array shape =',ds1ev.shape

    #print 'Subtract pedestals, if they were not subtracted in translator...'
    #ped_fname = '/reg/neh/home/dubrovin/LCLS/CSPadPedestals/cspad-pedestals-cxi49012-r0038.dat' # shape = (5920, 388)
    #ped_fname = '/reg/d/psdm/CXI/cxi49012/calib/CsPad::CalibV1/CxiDs1.0:Cspad.0/pedestals/9-37.data' # shape = (5920, 388)
    #ds1ev -= gm.getCSPadArrayFromFile(ped_fname)

    print 'Make the CSPad image from raw array'
    cspadimg = cip.CSPadImageProducer(calibpars, rotation=0, tiltIsOn=True)#, mirror=True)

    #arr = cspadimg.getImageArrayForCSPadElement( ds1ev )
    arr = cspadimg.getCSPadImage( ds1ev ) # This works faster

    print 'Plot CSPad image'
    AmpRange = (-10,90)
    gg.plotImage(arr,range=AmpRange,figsize=(11.6,10))
    #gg.move(200,100)
    gg.plotSpectrum(arr,range=AmpRange)
    #gg.move(50,50)
    #gg.plotImageAndSpectrum(arr,range=(1,2001))
    print 'To EXIT the test click on "x" in the top-right corner of each plot window.'
    gg.show()

#----------------------------------------------

def main_example_xpp() :

    print 'Start test in main_example_xpp()'

    #path_calib = '/reg/d/psdm/XPP/xpp36211/calib/CsPad::CalibV1/XppGon.0:Cspad.0'
    #path_calib = '/reg/neh/home/dubrovin/LCLS/CSPadAlignment-v01/calib-xpp36211-r0544'
    #path_calib = '/reg/d/psdm/xpp/xpp47712/calib/CsPad::CalibV1/XppGon.0:Cspad.0'
    path_calib = '/reg/d/psdm/XPP/xppcom10/calib/CsPad::CalibV1/XppGon.0:Cspad.0'


    #fname, runnum = '/reg/d/psdm/xpp/xpp36211/hdf5/xpp36211-r0073.h5', 73
    #fname, runnum = '/reg/d/psdm/xpp/xpp47712/hdf5/xpp47712-r0043.h5', 43
    fname, runnum = '/reg/d/psdm/XPP/xppcom10/hdf5/xppcom10-r1437.h5', 1437

    dsname = '/Configure:0000/Run:0000/CalibCycle:0000/CsPad::ElementV2/XppGon.0:Cspad.0/data'

    event = 0

    print 'Load calibration parameters from', path_calib
    calp.calibpars.setCalibParsForPath ( run=runnum, path=path_calib )

    print 'Get raw CSPad event %d from file %s \ndataset %s' % (event, fname, dsname)
    ds1ev = hm.getOneCSPadEventForTest( fname, dsname, event )
    #ds1ev = hm.getAverageCSPadEvent( fname, dsname, event, nevents=50 )
    print 'CSPad array shape =',ds1ev.shape

    #print 'Subtract pedestals, if they were not subtracted in translator...'
    #ped_fname = '/reg/neh/home/dubrovin/LCLS/CSPadPedestals/cspad-pedestals-cxi49012-r0038.dat' # shape = (5920, 388)
    #ds1ev -= gm.getCSPadArrayFromFile(ped_fname)

    print 'Make the CSPad image from raw array'
    #cspadimg = cip.CSPadImageProducer()
    cspadimg = cip.CSPadImageProducer(rotation=0, tiltIsOn=True) #, mirror=True)
    arr = cspadimg.getCSPadImage( ds1ev ) # This works faster

    print 'Plot CSPad image'
    AmpRange = (1600,2500)
    gg.plotImage(arr,range=AmpRange,figsize=(11.6,10))
    gg.move(200,100)
    gg.plotSpectrum(arr,range=AmpRange)
    gg.move(50,50)
    print 'To EXIT the test click on "x" in the top-right corner of each plot window.'
    gg.show()


#----------------------------------------------

def main_example_CSpad2x2() :

    print 'Start test in main_example_CSpad2x2()'

    fname = '/reg/d/psdm/xpp/xppi0212/hdf5/xppi0212-r0046.h5'
    dsname = '/Configure:0000/Run:0000/CalibCycle:0000/CsPad2x2::ElementV1/XppGon.0:Cspad2x2.0/data'
    event = 0

    h5file = hm.hdf5mets.open_hdf5_file(fname)
    #grp = hm.hdf5mets.get_dataset_from_hdf5_file('/')
    grp = hm.hdf5mets.get_dataset_from_hdf5_file('/Configure:0000/Run:0000/CalibCycle:0000/CsPad2x2::ElementV1')
    hm.print_hdf5_item_structure(grp)
    arrevts = hm.hdf5mets.get_dataset_from_hdf5_file(dsname)
    arr1ev = arrevts[event]
    hm.hdf5mets.close_hdf5_file()

    #print 'arr1ev=\n',       arr1ev
    print 'arr1ev.shape=\n', arr1ev.shape
    #arr = arr1ev[:,:,0]

    cspadimg = cip.CSPadImageProducer()
    arr = cspadimg.getImageArrayForCSpad2x2Element( arr1ev )

    AmpRange = (0,1200)
    gg.plotImage(arr,range=AmpRange,figsize=(11.6,10))
    gg.move(300,100)

    gg.plotSpectrum(arr,range=AmpRange)
    gg.move(10,100)

    gg.show()

#----------------------------------------------

def example_of_image_built_from_pix_coordinate_array_shaped_as_data() :
    """Some CSPAD segments may be missing in the dataset
    """

    fname, runnum = '/reg/d/psdm/CXI/cxi80410/hdf5/cxi80410-r0628.h5',  628
    dsname        = '/Configure:0000/Run:0000/CalibCycle:0000/CsPad::ElementV2/CxiDs1.0:Cspad.0/data'
    path_calib    = '/reg/d/psdm/CXI/cxi80410/calib/CsPad::CalibV1/CxiDs1.0:Cspad.0'
    Range         = (1000,3500)

    calp.calibpars.setCalibParsForPath (run=runnum, path=path_calib)
    #cpe.cpeval.printCalibParsEvaluated('center_global')
    cpe.cpeval.evaluateCSPadPixCoordinatesShapedAsData(fname,dsname,rotation=0)
    ds1ev = hm.getOneCSPadEventForTest( fname, dsname, event=0 ) # returns array with shape=(29, 185, 388)

    arr = cpe.cpeval.getTestImageShapedAsData(ds1ev)
    gg.plotImage(arr,range=Range,figsize=(11.6,10))
    gg.move(200,100)
    gg.show()

#----------------------------------------------

def example_of_image_built_from_pix_coordinate_array_for_entire_cspad() :
    """All CSPAD segments are assumed to be presented in this dataset
    """

    fname, runnum = '/reg/d/psdm/XPP/xppcom10/hdf5/xppcom10-r1437.h5', 1437
    dsname        = '/Configure:0000/Run:0000/CalibCycle:0000/CsPad::ElementV2/XppGon.0:Cspad.0/data'
    path_calib    = '/reg/d/psdm/XPP/xppcom10/calib/CsPad::CalibV1/XppGon.0:Cspad.0'
    Range         = (1700,2000)

    calp.calibpars.setCalibParsForPath (run=runnum, path=path_calib)
    #cpe.cpeval.printCalibParsEvaluated ('center_global')
    cpe.cpeval.evaluateCSPadPixCoordinates (rotation=0)
    ds1ev = hm.getOneCSPadEventForTest (fname, dsname, event=0) # returns array with shape=(32, 185, 388)

    arr = cpe.cpeval.getTestImageForEntireArray(ds1ev)
    gg.plotImage(arr,range=Range,figsize=(11.6,10))
    gg.move(200,100)
    gg.show()

#------------------------------

def test_cspad_image() :
    """Test of instantiation with external parameters.
    """
    run   = 150
    #path  = '/reg/neh/home1/dubrovin/LCLS/CSPadAlignment-v01/calib-xpp-2013-01-29'
    path  = '/reg/d/psdm/xpp/xpptut13/calib/CsPad::CalibV1/XppGon.0:Cspad.0/'
    calib = calp.CalibPars(path, run)
    coord = pixcoor.CSPADPixCoords(calib)
    #coord = pixcoor.CSPADPixCoords() # Default constructor
    coord.print_cspad_geometry_pars()

    event = 0
    fname  = '/reg/d/psdm/xpp/xpp66213/hdf5/xpp66213-r0150.h5'
    dsname = '/Configure:0000/Run:0000/CalibCycle:0000/CsPad::ElementV2/XppGon.0:Cspad.0/data'
    ds1ev = hm.getOneCSPadEventForTest( fname, dsname, event )
    #ds1ev = hm.getAverageCSPadEvent( fname, dsname, event=200, nevents=500 )
 
    ped_fname = '/reg/neh/home1/dubrovin/LCLS/CSPadPedestals/cspad-pedestals-xpp66213-r0149.dat' # shape = (5920, 388)
    peds = gm.getCSPadArrayFromFile(ped_fname)
    print 'peds.shape:', peds.shape
    #peds = calib.getCalibPars('pedestals')

    ds1ev -= peds
    img2d = coord.get_cspad_image(ds1ev)
    print 'img2d.shape =', img2d.shape
    
    gg.plotImageLarge(img2d, amp_range=(-10, 200), figsize=(12,11))
    gg.savefig('cspad-img.png')
    gg.show()

#----------------------------------------------

if __name__ == "__main__" :
    if len(sys.argv)==1   : print 'Use command: python', sys.argv[0], '<test-number=1, 10-13, 20-22, 51-55>'
    elif sys.argv[1]=='1' : test_cspad_image()

    elif sys.argv[1]=='10': pixcoor.test_cspadpixcoords_0()
    elif sys.argv[1]=='11': pixcoor.test_cspadpixcoords_1()
    elif sys.argv[1]=='12': pixcoor.test_cspadpixcoords_2()
    elif sys.argv[1]=='13': pixcoor.test_cspadpixcoords_3()

    elif sys.argv[1]=='20': pixcoor2x1.test_2x1_xy_maps()
    elif sys.argv[1]=='21': pixcoor2x1.test_2x1_img()
    elif sys.argv[1]=='22': pixcoor2x1.test_2x1_img_easy()()

    elif sys.argv[1]=='51' : main_example_cxi()
    elif sys.argv[1]=='52' : main_example_xpp()
    elif sys.argv[1]=='53' : example_of_image_built_from_pix_coordinate_array_shaped_as_data()
    elif sys.argv[1]=='54' : example_of_image_built_from_pix_coordinate_array_for_entire_cspad()
    elif sys.argv[1]=='55' : main_example_CSpad2x2()
    
    else : print 'Non-expected arguments: sys.argv=', sys.argv

    sys.exit ( 'End of test.' )

#----------------------------------------------
