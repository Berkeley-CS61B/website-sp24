package core;

import edu.princeton.cs.algs4.StdDraw;
import tileengine.TERenderer;
import tileengine.TETile;
import tileengine.Tileset;

import java.awt.*;
import java.util.Arrays;

public class FlowerWorld {
    public static final int WORLD_WIDTH = 80;
    public static final int WORLD_HEIGHT = 40;

    public static void main(String[] args) {
        // create renderer
        TERenderer ter = new TERenderer();
        ter.initialize(WORLD_WIDTH, WORLD_HEIGHT, 0, 0);

        // draw main menu
        StdDraw.setFont(new Font("Monaco", Font.BOLD, 50));
        StdDraw.setPenColor(Color.WHITE);
        StdDraw.text(WORLD_WIDTH * 0.5, WORLD_HEIGHT * 0.75, "Press any key to continue");
        StdDraw.show();
        while (!StdDraw.hasNextKeyTyped()) {
            StdDraw.pause(10);
        }

        // create flower world
        TETile[][] tiles = new TETile[WORLD_WIDTH][WORLD_HEIGHT];
        for (TETile[] ar : tiles) {
            Arrays.fill(ar, Tileset.NOTHING);
        }
        for (int x = WORLD_WIDTH / 4; x < WORLD_WIDTH * 3 / 4; x++) {
            for (int y = WORLD_HEIGHT / 4; y < WORLD_HEIGHT * 3 / 4; y++) {
                tiles[x][y] = Tileset.FLOWER;
            }
        }

        // render frame
        ter.renderFrame(tiles);
    }
}
