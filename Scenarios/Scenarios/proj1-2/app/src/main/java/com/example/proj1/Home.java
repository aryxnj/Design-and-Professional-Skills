package com.example.proj1;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;

public class Home extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_home);
        Button easyMode = (Button) findViewById(R.id.easyMode);
        final Intent easyQuestionPage = new Intent(this, easyModeQuestions.class);
        easyMode.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                startActivity(easyQuestionPage);
            }
        });
        final Intent mediumQuestionPage = new Intent(this, mediumModeQuestions.class);
        Button mediumMode = (Button) findViewById(R.id.mediumMode);
        mediumMode.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                startActivity(mediumQuestionPage);
            }
        });
        final Intent hardQuestionPage = new Intent(this, hardModeQuestions.class);
        Button hardMode = (Button) findViewById(R.id.hardMode);
        hardMode.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                startActivity(hardQuestionPage);
            }
        });
        final Intent createQuestion = new Intent(this, createYourOwnQuestion.class);
        Button createQ = (Button) findViewById(R.id.createQuestion);
        createQ.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                startActivity(createQuestion);
            }
        });
        final Intent answerQ = new Intent(this, AnswerOwnQuestions.class);
        Button answerQ1 = (Button) findViewById(R.id.answerOwnQuestions);
        answerQ1.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                startActivity(answerQ);
            }
        });
    }
}