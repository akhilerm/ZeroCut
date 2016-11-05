package com.slateandpencil.zerocut.desktop;

import com.badlogic.gdx.backends.lwjgl.LwjglApplication;
import com.badlogic.gdx.backends.lwjgl.LwjglApplicationConfiguration;
import com.slateandpencil.zerocut.ZeroCut;

import java.nio.file.Files;

public class DesktopLauncher {
	public static void main (String[] arg) {
		LwjglApplicationConfiguration config = new LwjglApplicationConfiguration();
		config.addIcon("ic_launcher_128.png", com.badlogic.gdx.Files.FileType.Internal);
        config.addIcon("ic_launcher_32.png", com.badlogic.gdx.Files.FileType.Internal);
        config.addIcon("ic_launcher_16.png", com.badlogic.gdx.Files.FileType.Internal);
		new LwjglApplication(new ZeroCut(), config);
	}
}
