package com.example.proj1;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.text.Html;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;

import com.chaquo.python.PyObject;
import com.chaquo.python.Python;
import com.chaquo.python.android.AndroidPlatform;

public class mediumModeQuestions extends AppCompatActivity {
    private static String question;
    private static String diffInt;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_medium_mode_questions);
        TextView questionText = (TextView) findViewById(R.id.question);
        if(!Python.isStarted()){
            Python.start(new AndroidPlatform(this));
        }
        Python py = Python.getInstance();
//        PyObject py1 = pyObject.callAttr("run1");
//        questionText.setText("Find differential of y = " + (py1.toString()));
//        question = py1.toString();
        TextView outputTest = (TextView) findViewById(R.id.question);
        Button submitAnswer = (Button) findViewById(R.id.checkAnswer);
        EditText answerEntry = (EditText) findViewById(R.id.userInput);
        if(!Python.isStarted()){
            Python.start(new AndroidPlatform(this));
        }
        Python py1 = Python.getInstance();
        final PyObject pyObject3 = py1.getModule("mediumQuestions");
        final Intent questionStyle1 = new Intent(this, mediumModeQuestions.class);
        PyObject py5 = pyObject3.callAttr("med_question");
        if (py5.toJava(String[].class)[1].equals("Differentiation")){
            diffInt = "Differentiation";
            questionText.setText("Differentiate the function: f(x) = " + py5.toJava(String[].class)[0]);
            question = py5.toJava(String[].class)[0];
        }else {
            diffInt = "Integration";
            questionText.setText("Integrate the function: f(x) = " + py5.toJava(String[].class)[0]);
            question = py5.toJava(String[].class)[0];
        }
        if(!Python.isStarted()){
            Python.start(new AndroidPlatform(this));
        }
        Python py2 = Python.getInstance();
        final PyObject pyObject = py2.getModule("sampleQuestionGenerator");
        final Intent questionStyle2 = new Intent(this, mediumModeQuestions.class);
        submitAnswer.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                String answer = answerEntry.getText().toString();
                PyObject py1 = pyObject.callAttr("userValidation", question, answer, diffInt);
                TextView textCheck = (TextView) findViewById(R.id.correctAnswer);
                textCheck.setText(py1.toString());
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