package com.slateandpencil.zerocut.board;

import com.badlogic.gdx.Gdx;

/**
 * Created by Akhil on 06-11-2016.
 */

public class Board {
    public static final String TAG = Board.class.getName();
    Cell[][] cells;

    public Board() {
        this.cells = new Cell[9][9];
        for (int r = 0; r < 9; r++){
            for (int c =0; c < 9; c++){
                cells[r][c] = new Cell(new CellPosition(r%3, c%3, r/3, c/3));
            }
        }
    }

    public Board(Board board) {
        this.cells = new Cell[9][9];
        for (int r = 0; r < 9; r++){
            for (int c = 0; c < 9; c++){
                cells[r][c] = new Cell(board.cells[r][c]);
            }
        }
    }

    public boolean setCell(CellPosition position, Cell.CellValue value) {
        if(cells[position.sub_r*3+position.r][position.sub_c*3+position.c].value == Cell.CellValue.EMPTY) {
            cells[position.sub_r*3+position.r][position.sub_c*3+position.c].value = value;
            return true;
        }
        else {
            Gdx.app.log(TAG,"Cell already filled");
            return false;
        }
    }

    public void clearBoard() {
        this.cells = new Cell[9][9];
        for (int r = 0; r < 9; r++){
            for (int c = 0; c < 9; c++){
                cells[r][c] = new Cell(new CellPosition(r%3, c%3, r/3, c/3));
            }
        }
    }
}