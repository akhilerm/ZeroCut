package com.slateandpencil.zerocut.ai;

import com.slateandpencil.zerocut.board.Board;
import com.slateandpencil.zerocut.board.CellPosition;
import com.slateandpencil.zerocut.player.Player;

/**
 * Created by Akhil on 06-11-2016.
 */

public interface AI {
    CellPosition determineBestPosition(Board board, Player forPlayer);
}
