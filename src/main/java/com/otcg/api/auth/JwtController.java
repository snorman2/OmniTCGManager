package com.otcg.api.auth;

import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

@SpringBootApplication
@RestController
public class JwtController {
    @GetMapping("/auth/token")
    public ResponseEntity getToken(){

        return new ResponseEntity<String>("Authenticated", HttpStatus.OK);
    }
}
