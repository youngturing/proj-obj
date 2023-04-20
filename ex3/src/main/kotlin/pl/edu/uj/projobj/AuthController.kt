package pl.edu.uj.projobj

import org.springframework.beans.factory.annotation.Autowired
import org.springframework.web.bind.annotation.PostMapping
import org.springframework.web.bind.annotation.RequestBody
import org.springframework.web.bind.annotation.RestController

@RestController
class AuthorizationController {

  @Autowired
  private lateinit var authorizationService: AuthorizationService
  
  @PostMapping("/login")
  fun login(@RequestBody loginRequest: LoginRequest): LoginResponse {
    val isAuthorized = authorizationService.authorizeUser(loginRequest.username, loginRequest.password)
    return LoginResponse(isAuthorized)
  }
  
}

data class LoginRequest(val username: String, val password: String)
data class LoginResponse(val isAuthorized: Boolean)
