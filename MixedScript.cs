using UnityEngine;
using UnityEngine.InputSystem;

public class MixedScript : MonoBehaviour
{
    private Renderer rend;
    public float moveSpeed = 10f;

    void Start()
    {
        rend = GetComponent<Renderer>();
    }

    void Update()
    {
        HandleMovement();
        HandleMouseClick();
    }

    // ---------- MOVEMENT ----------
    void HandleMovement()
    {
        float moveHorizontal = Input.GetAxis("Horizontal"); // A/D or Left/Right
        float moveVertical = Input.GetAxis("Vertical");     // W/S or Up/Down

        Vector3 movement = new Vector3(moveHorizontal, 0f, moveVertical);
        transform.Translate(movement * moveSpeed * Time.deltaTime, Space.World);
    }

    // ---------- COLOR CLICK ----------
    void HandleMouseClick()
    {
        if (Mouse.current != null && Mouse.current.leftButton.wasPressedThisFrame)
        {
            Ray ray = Camera.main.ScreenPointToRay(Mouse.current.position.ReadValue());

            if (Physics.Raycast(ray, out RaycastHit hit))
            {
                if (hit.transform == transform)
                {
                    rend.material.color = Random.ColorHSV();
                }
            }
        }
    }
}
