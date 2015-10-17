package com.example.krishnaghatia.rocktheearth;

import android.content.Intent;
import android.net.Uri;
import android.os.Environment;
import android.provider.MediaStore;
import android.support.v7.app.ActionBarActivity;
import android.os.Bundle;
import android.util.Log;
import android.view.Menu;
import android.view.MenuItem;
import android.view.View;
import android.widget.ImageButton;
import android.widget.ListView;

import java.io.File;
import java.text.SimpleDateFormat;
import java.util.Date;


public class HomePage extends ActionBarActivity {

    private static final int CAPTURE_IMAGE_ACTIVITY_REQUEST_CODE = 100;

    ImageButton btnCamera;
    ImageButton btnSignUp;
    ListView campaignList;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_home_page);

        grabComponents();
        addListeners();
    }

    private void grabComponents() {
        //camera button
        btnCamera = (ImageButton) findViewById(R.id.btnCamera);
        btnCamera.setImageResource(R.mipmap.ic_launcher);

        //signUp form button
        btnSignUp = (ImageButton) findViewById(R.id.btnSignUp);
        btnSignUp.setImageResource(R.mipmap.ic_signup);

        //campaigns list uses customListAdapter class
        campaignList = (ListView) findViewById(R.id.lvCampaigns);
        campaignList.setAdapter(new customListAdapter(this.getLayoutInflater()));
    }



    private void addListeners() {
        btnCamera.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent cameraIntent = new Intent(MediaStore.ACTION_IMAGE_CAPTURE);
                startActivityForResult(cameraIntent, CAPTURE_IMAGE_ACTIVITY_REQUEST_CODE);
            }
        });
    }


    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        // Inflate the menu; this adds items to the action bar if it is present.
        getMenuInflater().inflate(R.menu.menu_home_page, menu);
        return true;
    }

    @Override
    public boolean onOptionsItemSelected(MenuItem item) {
        // Handle action bar item clicks here. The action bar will
        // automatically handle clicks on the Home/Up button, so long
        // as you specify a parent activity in AndroidManifest.xml.
        int id = item.getItemId();

        //noinspection SimplifiableIfStatement
        if (id == R.id.action_settings) {
            return true;
        }

        return super.onOptionsItemSelected(item);
    }
}
