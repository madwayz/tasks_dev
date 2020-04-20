package com.example.dnsresolver;

import androidx.appcompat.app.AppCompatActivity;

import android.annotation.SuppressLint;
import android.graphics.Color;
import android.os.Bundle;
import android.text.Editable;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;

import com.android.volley.Request;
import com.android.volley.RequestQueue;
import com.android.volley.Response;
import com.android.volley.VolleyError;
import com.android.volley.toolbox.JsonArrayRequest;
import com.android.volley.toolbox.JsonObjectRequest;
import com.android.volley.toolbox.Volley;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

public class MainActivity extends AppCompatActivity {
    public static Button button1;
    public static TextView textView1;
    public static EditText editText1;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        button1 = findViewById(R.id.button1);
        textView1 = findViewById(R.id.textView1);
        editText1 = findViewById(R.id.editText1);

        button1.setOnClickListener(new View.OnClickListener() {
            @SuppressLint("ResourceAsColor")
            @Override
            public void onClick(View v) {
                getDomainInfo(editText1.getText());
            }
        });
    }

    private void getDomainInfo(Editable domain) {
        String URI = "http://149.154.71.26:7070/resolve?domain=" + domain;
        RequestQueue rq = Volley.newRequestQueue(this);
        JsonObjectRequest jOR = new JsonObjectRequest(Request.Method.GET, URI,null,
                new Response.Listener<JSONObject>() {
                    @Override
                    public void onResponse(JSONObject response) {
                        try {
                            textView1.setText(
                                    String.format("Organization: %s\n" +
                                            "City: %s\nCountry: %s\n" +
                                            "Country code: %s\n" +
                                            "ISP: %s\n" +
                                            "Latitude: %s\n" +
                                            "Longitude: %s\n" +
                                            "IP: %s",
                                            response.getString("org"),
                                            response.getString("city"),
                                            response.getString("country"),
                                            response.getString("countryCode"),
                                            response.getString("isp"),
                                            response.getDouble("lat"),
                                            response.getDouble("lon"),
                                            response.getString("query")));
                        } catch (JSONException ex) {
                            ex.printStackTrace();
                        }
                    }
                },
                new Response.ErrorListener() {
                    @Override
                    public void onErrorResponse(VolleyError error) {

                    }
                });
        rq.add(jOR);
    }
}


