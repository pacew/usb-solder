import sys
import importlib

sys.path.append('/usr/lib/python3/dist-packages')
import pcbnew
from pcbnew import ToMM, FromMM

def delete_middle_tracks(board):
    region_left = FromMM(70)
    region_top = FromMM(0)
    region_right = FromMM(130)
    region_bottom = FromMM(130)

    del_tracks = []
    for track in board.GetTracks():
        start = track.GetStart()
        end = track.GetEnd()

        left = min(start.x, end.x)
        right = max(start.x, end.x)
        top = min(start.y, end.y)
        bottom = max(start.y, end.y)

        if (region_left < left and right < region_right
            and region_top < top and bottom < region_bottom):
            del_tracks.append(track)

    for track in del_tracks:
        board.Delete(track)

filename = 'usb-solder.kicad_pcb'
board = pcbnew.LoadBoard(filename)
delete_middle_tracks(board)
board.Save(filename)
