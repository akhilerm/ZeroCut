package com.slateandpencil.zerocut.player;

import com.slateandpencil.zerocut.board.Board;
import com.slateandpencil.zerocut.board.CellPosition;

/**
 * Created by Akhil on 06-11-2016.
 */

public class AIPlayer extends Player {
    public static final String TAG = Player.class.getName();

    public AIPlayer(Board board, PlayerType type) {
        super(board, type);
    }

    public CellPosition makeAIMove() {
        CellPosition bestPosition  = determineBestPosition(board);
        board.setCell(bestPosition, playerType.getCellValue());
        return bestPosition;
    }
}
