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

public class register extends AppCompatActivity{
    private static String username = "abc123444";
    private static String password = "abc123444dm,nds,jdnsjkdanjk";
    private static String a;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_register);
        Button button1 = (Button) findViewById(R.id.buttonClick);
        final EditText input1 = (EditText) findViewById(R.id.usernameEntry);
        final EditText input2 = (EditText) findViewById(R.id.passwordEntry);
        final TextView output1 = (TextView) findViewById(R.id.output1);
        if(!Python.isStarted()){
            Python.start(new AndroidPlatform(this));
        }
        Python py = Python.getInstance();
        final PyObject pyObject = py.getModule("test");
        final Intent signIn1 = new Intent(this, MainActivity.class);
        button1.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                String textInput = input1.getText().toString();
                input1.setText("");
                String textInput1 = input2.getText().toString();
                input2.setText("");
                PyObject py1 = pyObject.callAttr("main", textInput, textInput1);
                output1.setText(py1.toString());
                if(py1.toString().equals("User created successfully")){
                    startActivity(signIn1);
                }
            }
        });
    }
}