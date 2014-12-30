Rails.application.routes.draw do
  resources :visits, only: [:index, :create]
  resources :recommendation, only: [:index]

  root 'welcome#index'
end
