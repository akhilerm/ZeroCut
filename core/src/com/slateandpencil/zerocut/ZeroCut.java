package com.slateandpencil.zerocut;

import com.badlogic.gdx.ApplicationAdapter;
import com.badlogic.gdx.Gdx;
import com.badlogic.gdx.graphics.GL20;
import com.badlogic.gdx.graphics.Texture;
import com.badlogic.gdx.graphics.g2d.SpriteBatch;

public class ZeroCut extends ApplicationAdapter {
	SpriteBatch batch;
	//Texture img;
	
	@Override
	public void create () {
		batch = new SpriteBatch();
		//img = new Texture("ic_launcher_128.png");
	}

	@Override
	public void render () {
		Gdx.gl.glClearColor(76/255f, 175/255f, 80/255f, 1);
		Gdx.gl.glClear(GL20.GL_COLOR_BUFFER_BIT);
		batch.begin();
		//batch.draw(img, 50, 50);
		batch.end();
	}
	
	@Override
	public void dispose () {
		batch.dispose();
		//img.dispose();
	}
}
