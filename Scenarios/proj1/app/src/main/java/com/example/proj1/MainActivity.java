package com.example.proj1;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;

import com.chaquo.python.PyObject;
import com.chaquo.python.Python;
import com.chaquo.python.android.AndroidPlatform;

public class MainActivity extends AppCompatActivity {
    private static String username = "abc123444";
    private static String password = "abc123444dm,nds,jdnsjkdanjk";
    private static String a;
    public static String usernameFinal;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        Button button1 = (Button) findViewById(R.id.buttonAtr1);
        final EditText input1 = (EditText) findViewById(R.id.textEntryUsername);
        final EditText input2 = (EditText) findViewById(R.id.textEntryPassword);
        final TextView output1 = (TextView) findViewById(R.id.textAtr1);
        final Button button2 = (Button) findViewById(R.id.buttonNext);
        final Intent register1 = new Intent(this, register.class);
        button2.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                startActivity(register1);
            }
        });
        if(!Python.isStarted()){
                    Python.start(new AndroidPlatform(this));
                }
        Python py = Python.getInstance();
        final PyObject pyObject = py.getModule("signInAuth");
        final Intent questionStyle1 = new Intent(this, questionStyle.class);
        final Intent homePage = new Intent(this, Home.class);
        button1.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                String textInput = input1.getText().toString();
                input1.setText("");
                String textInput1 = input2.getText().toString();
                input2.setText("");
                PyObject py1 = pyObject.callAttr("main", textInput, textInput1);
                output1.setText(py1.toString());
                if(py1.toString().equals("Accepted")){
                    usernameFinal = textInput;
                    startActivity(homePage);
                }
            }
        });


    }
}