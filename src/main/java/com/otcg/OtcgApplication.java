package com.otcg;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.EnableAutoConfiguration;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.ComponentScan;

@SpringBootApplication

public class OtcgApplication {

    public static void main(String[] args) {
        SpringApplication.run(OtcgApplication.class, args);
    }
}
