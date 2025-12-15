using UnityEngine;

[RequireComponent(typeof(Renderer))]
[RequireComponent(typeof(Collider))]
public class ChangeColorOnClick : MonoBehaviour
{
    private Renderer rend;

    void Awake()
    {
        rend = GetComponent<Renderer>();
    }

    void OnMouseDown()
    {
        rend.material.color = Random.ColorHSV();
    }
}
