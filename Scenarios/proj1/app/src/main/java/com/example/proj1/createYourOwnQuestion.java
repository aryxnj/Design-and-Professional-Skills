package com.example.proj1;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;

import com.chaquo.python.PyObject;
import com.chaquo.python.Python;
import com.chaquo.python.android.AndroidPlatform;

public class createYourOwnQuestion extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_create_your_own_question);
        EditText question = (EditText) findViewById(R.id.questionName);
        EditText solution = (EditText) findViewById(R.id.solutionName);
        Button submit = (Button) findViewById(R.id.add1);
        if(!Python.isStarted()){
            Python.start(new AndroidPlatform(this));
        }
        Python py1 = Python.getInstance();
        final PyObject pyObject3 = py1.getModule("questionAnswers");
        final Intent questionStyle1 = new Intent(this, createYourOwnQuestion.class);
        final Intent home = new Intent(this, Home.class);
        submit.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                PyObject py5 = pyObject3.callAttr("upload", question.getText().toString(), solution.getText().toString());
                startActivity(home);
            }
        });

    }
}