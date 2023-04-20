package pl.edu.uj.projobj

import org.springframework.stereotype.Service

@Service(lazy=true)
class AuthorizationService {
  
  private val authorizedUsers = listOf(
    User("Alice", "password1"),
    User("Bob", "password2")
  )

  fun authorizeUser(username: String, password: String): Boolean {
    return authorizedUsers.any { it.username == username && it.password == password }
  }
  
}

data class User(val username: String, val password: String)
