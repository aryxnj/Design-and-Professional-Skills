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

public class easyModeQuestions extends AppCompatActivity {
    private static int countAddMore;
    private static String diffInt;
    private static String question;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_easy_mode_questions);
        if(!Python.isStarted()){
            Python.start(new AndroidPlatform(this));
        }
        Python py = Python.getInstance();
        TextView questionText = (TextView) findViewById(R.id.question);
        final PyObject pyObject = py.getModule("easyQuestions");
        PyObject py1 = pyObject.callAttr("easy_question");
        diffInt = py1.toJava(String[].class)[1];
        question = py1.toJava(String[].class)[0];
        if (py1.toJava(String[].class)[1].equals("Differentiation")){
            questionText.setText("Differentiate the function: f(x) = " + py1.toJava(String[].class)[0]);

        }else {
            questionText.setText("Integrate the function: f(x) = " + py1.toJava(String[].class)[0]);
        }

        Button more = (Button) findViewById(R.id.addMore);
        more.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                if (countAddMore == 0) {
                    EditText add = (EditText) findViewById(R.id.add1);
                    add.setText("");
                    add.setVisibility(View.VISIBLE);
                } else if (countAddMore == 1) {
                    EditText add = (EditText) findViewById(R.id.add2);
                    add.setText("");
                    add.setVisibility(View.VISIBLE);
                } else if (countAddMore == 2) {
                    TextView add = (EditText) findViewById(R.id.add3);
                    add.setText("");
                    add.setVisibility(View.VISIBLE);
                } else if (countAddMore == 3) {
                    EditText add = (EditText) findViewById(R.id.add4);
                    add.setText("");
                    add.setVisibility(View.VISIBLE);
                } else if (countAddMore == 4) {
                    EditText add = (EditText) findViewById(R.id.add5);
                    add.setText("");
                    add.setVisibility(View.VISIBLE);
                } else {
                    countAddMore = 0;
                }
                countAddMore++;
            }
        });
        Button minusOne = (Button) findViewById(R.id.minusOne);
        minusOne.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                TextView add = (EditText) findViewById(R.id.add1);
                add.setVisibility(View.INVISIBLE);
                add = (EditText) findViewById(R.id.add2);
                add.setVisibility(View.INVISIBLE);
                add = (EditText) findViewById(R.id.add3);
                add.setVisibility(View.INVISIBLE);
                add = (EditText) findViewById(R.id.add4);
                add.setVisibility(View.INVISIBLE);
                add = (EditText) findViewById(R.id.add5);
                add.setVisibility(View.INVISIBLE);
                countAddMore = 0;
            }
        });
        TextView outputTest = (TextView) findViewById(R.id.testDelete);
        Button submitAnswer = (Button) findViewById(R.id.submitAnswer);
        if(!Python.isStarted()){
            Python.start(new AndroidPlatform(this));
        }
        Python py2 = Python.getInstance();
        final PyObject pyObject3 = py2.getModule("sampleQuestionGenerator");
        final Intent questionStyle2 = new Intent(this, easyModeQuestions.class);
        EditText submit3 = (EditText) findViewById(R.id.userInput2);

        submitAnswer.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                String answer = submit3.getText().toString();
                PyObject py1 = pyObject3.callAttr("userValidation", question, answer, diffInt);
                TextView textCheck = (TextView) findViewById(R.id.correctAnswer);
//                    textCheck.setText(py1.toString());
                outputTest.setText(py1.toString());
//
        }});
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