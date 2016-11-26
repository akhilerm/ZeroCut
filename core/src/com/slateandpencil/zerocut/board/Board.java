package com.slateandpencil.zerocut.board;

import com.badlogic.gdx.Gdx;
import com.slateandpencil.zerocut.board.Cell.*;

import java.util.ArrayList;
import java.util.List;

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

    public int getScore(){
        int totalScore=0;
        /*
         insert code to find score of a move
         */
        return totalScore;
    }

    public Results getResults(){
        Results tempResults = new Results();
        /*
        insert code for result
         */
        return tempResults;
    }

    public boolean setCell(CellPosition position, CellValue value) {
        if(cells[position.sub_r*3+position.r][position.sub_c*3+position.c].value == CellValue.EMPTY) {
            cells[position.sub_r*3+position.r][position.sub_c*3+position.c].value = value;
            return true;
        }
        else {
            Gdx.app.log(TAG,"Cell already filled");
            return false;
        }
    }

    public List<CellPosition> emptyCellPositions() {
        List<CellPosition> positions = new ArrayList<CellPosition>();
        for (int i = 0; i < cells.length; i++) {
            for (int x = 0; x < cells[i].length; x++) {
                if (cells[i][x].value == CellValue.EMPTY) {
                    positions.add(cells[i][x].position);
                }
            }
        }
        return positions;
    }

    public void clearBoard() {
        this.cells = new Cell[9][9];
        for (int r = 0; r < 9; r++){
            for (int c = 0; c < 9; c++){
                cells[r][c] = new Cell(new CellPosition(r%3, c%3, r/3, c/3));
            }
        }
    }

    public Cell cellAtPosition(CellPosition position) {
        return cells[position.sub_r*3+position.r][position.sub_c*3+position.c];
    }

    public Board boardAfterMove(CellPosition position, CellValue value) {
        Board nextBoard = new Board(this);
        nextBoard.cells[position.sub_r*3+position.r][position.sub_c*3+position.c].position = position;
        nextBoard.cells[position.sub_r*3+position.r][position.sub_c*3+position.c].value = value;
        return nextBoard;
    }

    public Boolean gameOver() {
        return getResults().hasWinner == true || emptyCellPositions().size() == 0;
    }
}