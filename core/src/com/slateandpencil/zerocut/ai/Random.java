package com.slateandpencil.zerocut.ai;

import com.slateandpencil.zerocut.board.Board;
import com.slateandpencil.zerocut.board.CellPosition;
import com.slateandpencil.zerocut.player.Player;
import java.util.List;
import com.badlogic.gdx.math.MathUtils;

/**
 * Created by Akhil on 23-12-2016.
 */

public class Random implements AI{

    public static final String TAG = Random.class.getName();

    public CellPosition determineBestPosition(Board board, Playrer forPlayer){
        List<CellPosition> availableCells = board.emptyCellPositions();
        int randomIndex = MathUtils.random(0,availableCells.size()-1);
        return availableCells.get(randomIndex);
    }

}