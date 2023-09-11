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

public class AnswerOwnQuestions extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_answer_own_questions);
        TextView question = (TextView) findViewById(R.id.questionName);
        EditText solution = (EditText) findViewById(R.id.solutionName2);
        Button submit = (Button) findViewById(R.id.add6);
        Button nextButton = (Button) findViewById(R.id.nextButton);
        if(!Python.isStarted()){
            Python.start(new AndroidPlatform(this));
        }
        Python py1 = Python.getInstance();
        final PyObject pyObject3 = py1.getModule("questionAnswers");
        final Intent questionStyle1 = new Intent(this, AnswerOwnQuestions.class);
//        final Intent home = new Intent(this, Home.class);
        PyObject py5 = pyObject3.callAttr("readRandom");
        question.setText(py5.toJava(String[].class)[0].toString());
        TextView abc = (TextView) findViewById(R.id.validation);
        submit.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                if (solution.getText().toString().equals(py5.toJava(String[].class)[1].toString())){
                    abc.setText("Correct");
                } else{
                    abc.setText("Wrong");
                }
            }
        });
        Button nextButton1 = (Button) findViewById(R.id.nextButton);
        nextButton1.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Intent intent = getIntent();
                finish();
                startActivity(intent);
            }
        });

    }
}