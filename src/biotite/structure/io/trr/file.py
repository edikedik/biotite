# Copyright 2017 Patrick Kunzmann.
# This source code is part of the Biotite package and is distributed under the
# 3-Clause BSD License.  Please see 'LICENSE.rst' for further information.

from ..trajfile import TrajectoryFile

__all__ = ["TRRFile"]


class TRRFile(TrajectoryFile):
    """
    This file class represents a TRR trajectory file.
    """
    
    def traj_type(self):
        import mdtraj.formats as traj
        return traj.TRRTrajectoryFile
    
    def output_value_index(self, value):
        if value == "coord":
            return 0
        if value == "time":
            return 1
        if value == "box":
            return 3