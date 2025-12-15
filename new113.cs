using UnityEngine;
using UnityEngine.InputSystem;

public class new113 : MonoBehaviour
{
    private Renderer objRenderer;

    void Start()
    {
        objRenderer = GetComponent<Renderer>();
    }
    void Update()
    {
        float movespeed = 5f;
        float moveX = 0f;
        float moveZ = 0f;

        if (Keyboard.current != null)
        {

               if (Keyboard.current.aKey.isPressed) moveX -= 1f;
               if (Keyboard.current.dKey.isPressed) moveX += 1f;
               if (Keyboard.current.wKey.isPressed) moveZ += 1f;
               if (Keyboard.current.sKey.isPressed) moveZ -= 1f;
        }
         Vector3 move = new Vector3(moveX, 0, moveZ).normalized * movespeed * Time.deltaTime;   
        
    } 
}